package dev.vladimiracuna.aidatasetfoundry;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;

final class DatasetBuilder {
    private DatasetBuilder() {}

    static List<String> chunk(String sourceName, String rawText, int maxChars) {
        String normalized = rawText.replace("\r\n", "\n").replace('\r', '\n').trim();
        List<String> result = new ArrayList<>();
        StringBuilder current = new StringBuilder();
        for (String paragraph : normalized.split("\\n\\s*\\n")) {
            String clean = paragraph.replaceAll("[\\t ]+", " ").trim();
            if (clean.isEmpty()) continue;
            if (current.length() > 0 && current.length() + clean.length() + 2 > maxChars) {
                addRecord(result, sourceName, current.toString());
                current.setLength(0);
            }
            if (clean.length() > maxChars) {
                if (current.length() > 0) {
                    addRecord(result, sourceName, current.toString());
                    current.setLength(0);
                }
                for (int start = 0; start < clean.length(); start += maxChars) {
                    addRecord(result, sourceName, clean.substring(start, Math.min(start + maxChars, clean.length())));
                }
            } else {
                if (current.length() > 0) current.append("\n\n");
                current.append(clean);
            }
        }
        if (current.length() > 0) addRecord(result, sourceName, current.toString());
        return result;
    }

    private static void addRecord(List<String> records, String sourceName, String text) {
        String contentHash = sha256(text);
        String documentId = "doc_" + sha256(sourceName).substring(0, 16);
        String id = "chunk_" + sha256(documentId + ":" + records.size() + ":" + contentHash).substring(0, 20);
        records.add("{\"id\":\"" + id + "\",\"document_id\":\"" + documentId
                + "\",\"text\":\"" + escape(text) + "\",\"source\":{\"kind\":\"android_document\",\"locator\":\""
                + escape(sourceName) + "\"},\"metadata\":{\"chunk_index\":" + records.size()
                + "},\"provenance\":{\"content_sha256\":\"" + contentHash + "\"}}" );
    }

    static String asJsonl(List<String> records) {
        return String.join("\n", records) + (records.isEmpty() ? "" : "\n");
    }

    private static String escape(String value) {
        return value.replace("\\", "\\\\").replace("\"", "\\\"")
                .replace("\n", "\\n").replace("\t", "\\t");
    }

    private static String sha256(String value) {
        try {
            byte[] digest = MessageDigest.getInstance("SHA-256").digest(value.getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder();
            for (byte item : digest) hex.append(String.format("%02x", item));
            return hex.toString();
        } catch (NoSuchAlgorithmException impossible) {
            throw new IllegalStateException(impossible);
        }
    }
}
