package dev.vladimiracuna.aidatasetfoundry;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.GradientDrawable;
import android.net.Uri;
import android.os.Bundle;
import android.provider.OpenableColumns;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public final class MainActivity extends Activity {
    private static final int PICK_DOCUMENT = 10;
    private static final int SAVE_DATASET = 11;
    private final List<String> records = new ArrayList<>();
    private TextView status;
    private Button export;

    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        setContentView(buildUi());
    }

    private ScrollView buildUi() {
        int pad = dp(24);
        ScrollView scroll = new ScrollView(this);
        scroll.setBackgroundColor(Color.rgb(248, 250, 252));
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(pad, pad, pad, pad);

        TextView badge = text("LOCAL · OFFLINE · v0.2.0", 12, Color.rgb(91, 91, 214));
        badge.setTypeface(null, 1);
        root.addView(badge);
        TextView title = text("Dataset Foundry", 31, Color.rgb(17, 24, 39));
        title.setTypeface(null, 1);
        title.setPadding(0, dp(8), 0, dp(8));
        root.addView(title);
        TextView intro = text("Convierte documentos de texto en registros JSONL trazables para experimentación con IA.", 17, Color.rgb(71, 85, 105));
        intro.setPadding(0, 0, 0, dp(24));
        root.addView(intro);

        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setPadding(dp(20), dp(20), dp(20), dp(20));
        GradientDrawable background = new GradientDrawable();
        background.setColor(Color.WHITE);
        background.setCornerRadius(dp(18));
        background.setStroke(dp(1), Color.rgb(226, 232, 240));
        card.setBackground(background);

        Button select = button("Elegir TXT, Markdown, JSON o CSV");
        select.setOnClickListener(v -> pickDocument());
        card.addView(select);
        status = text("Ningún documento procesado.", 15, Color.rgb(71, 85, 105));
        status.setPadding(0, dp(18), 0, dp(18));
        card.addView(status);
        export = button("Exportar dataset.jsonl");
        export.setEnabled(false);
        export.setOnClickListener(v -> saveDataset());
        card.addView(export);
        root.addView(card, new LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));

        TextView note = text("Privacidad: la aplicación no solicita permiso de Internet. El contenido permanece en el dispositivo.", 14, Color.rgb(100, 116, 139));
        note.setPadding(0, dp(22), 0, 0);
        root.addView(note);
        scroll.addView(root);
        return scroll;
    }

    private void pickDocument() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT).setType("*/*").addCategory(Intent.CATEGORY_OPENABLE);
        intent.putExtra(Intent.EXTRA_MIME_TYPES, new String[]{"text/plain", "text/markdown", "application/json", "text/csv"});
        startActivityForResult(intent, PICK_DOCUMENT);
    }

    private void saveDataset() {
        Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT).setType("application/x-ndjson").putExtra(Intent.EXTRA_TITLE, "dataset.jsonl");
        startActivityForResult(intent, SAVE_DATASET);
    }

    @Override protected void onActivityResult(int request, int result, Intent data) {
        super.onActivityResult(request, result, data);
        if (result != RESULT_OK || data == null || data.getData() == null) return;
        try {
            if (request == PICK_DOCUMENT) load(data.getData());
            if (request == SAVE_DATASET) write(data.getData());
        } catch (Exception error) {
            Toast.makeText(this, error.getMessage(), Toast.LENGTH_LONG).show();
        }
    }

    private void load(Uri uri) throws Exception {
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(getContentResolver().openInputStream(uri), StandardCharsets.UTF_8))) {
            char[] buffer = new char[8192];
            int count;
            while ((count = reader.read(buffer)) >= 0) {
                content.append(buffer, 0, count);
                if (content.length() > 5_000_000) throw new IllegalArgumentException("El archivo supera el límite demo de 5 MB.");
            }
        }
        records.clear();
        records.addAll(DatasetBuilder.chunk(displayName(uri), content.toString(), 1200));
        status.setText(records.size() + " fragmentos listos · " + content.length() + " caracteres leídos");
        export.setEnabled(!records.isEmpty());
    }

    private void write(Uri uri) throws Exception {
        try (OutputStream output = getContentResolver().openOutputStream(uri)) {
            if (output == null) throw new IllegalStateException("No se pudo abrir el destino.");
            output.write(DatasetBuilder.asJsonl(records).getBytes(StandardCharsets.UTF_8));
        }
        Toast.makeText(this, "Dataset JSONL exportado.", Toast.LENGTH_LONG).show();
    }

    private String displayName(Uri uri) {
        try (android.database.Cursor cursor = getContentResolver().query(uri, null, null, null, null)) {
            if (cursor != null && cursor.moveToFirst()) {
                int index = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME);
                if (index >= 0) return cursor.getString(index);
            }
        }
        return "documento";
    }

    private Button button(String value) {
        Button button = new Button(this);
        button.setText(value);
        button.setTextSize(15);
        button.setAllCaps(false);
        button.setMinHeight(dp(52));
        return button;
    }

    private TextView text(String value, int size, int color) {
        TextView view = new TextView(this);
        view.setText(value);
        view.setTextSize(size);
        view.setTextColor(color);
        view.setGravity(Gravity.START);
        return view;
    }

    private int dp(int value) { return Math.round(value * getResources().getDisplayMetrics().density); }
}
