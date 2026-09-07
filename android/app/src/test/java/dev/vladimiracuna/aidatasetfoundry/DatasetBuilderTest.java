package dev.vladimiracuna.aidatasetfoundry;

import org.junit.Test;
import java.util.List;
import static org.junit.Assert.*;

public class DatasetBuilderTest {
    @Test public void exportsStableJsonlRecords() {
        List<String> records = DatasetBuilder.chunk("guide.md", "Primer párrafo suficientemente explicativo.\n\nSegundo párrafo.", 100);
        assertEquals(1, records.size());
        assertTrue(records.get(0).contains("\"document_id\""));
        assertTrue(records.get(0).contains("\"content_sha256\""));
        assertTrue(DatasetBuilder.asJsonl(records).endsWith("\n"));
    }

    @Test public void splitsOversizedText() {
        String value = "a".repeat(250);
        assertEquals(3, DatasetBuilder.chunk("large.txt", value, 100).size());
    }
}
