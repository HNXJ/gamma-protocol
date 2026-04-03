#include <stdio.h>
#include <string.h>
#include <ctype.h>

/**
 * Problem: Low-level system agents require a lightweight, zero-dependency GAMMA forge.
 * Solution: C implementation for direct hardware/OS-level trace generation.
 */
void forge_gamma(char *title, char *problem, char *solution, char *logic) {
    char *source = "gemini-cli";
    char *target = "any";
    char *digest = "This protocol mandates high-fidelity agentic action traces. Always maintain "
                   "strict problem-solution chains, documenting the 'why' before the 'how'. "
                   "Ensure every directive is autonomous, verifiable, and free of version suffixes. "
                   "Map deterministic targets using unified schemas. Execute terminal actions with "
                   "precision, registering every newly generated skill to the central ledger.";

    char filename[256];
    strncpy(filename, title, 250);
    for(int i = 0; filename[i]; i++) {
        filename[i] = tolower(filename[i]);
        if(filename[i] == ' ') filename[i] = '_';
    }
    strcat(filename, ".gamma");

    FILE *f = fopen(filename, "w");
    if (f == NULL) {
        printf("❌ Error: Could not create %s\n", filename);
        return;
    }

    fprintf(f, "# GAMMA: %s\n\n", title);
    fprintf(f, "**agent-source**: %s\n", source);
    fprintf(f, "**agent-target**: %s\n\n", target);
    fprintf(f, "## 🤖 For Agents\n%s\n\n", digest);
    fprintf(f, "## 1. Problem-Solution Architecture (The 'Why')\n\n");
    fprintf(f, "**Q: What is the primary bottleneck for this action?**\n");
    fprintf(f, "**Problem**: %s\n", problem);
    fprintf(f, "**Solution**: %s\n\n", solution);
    fprintf(f, "## 2. Execution Logic & Finality\n");
    fprintf(f, "**Logic**: %s\n\n", logic);
    fprintf(f, "## 3. Rules & Constraints\n");
    fprintf(f, "- **Non-Suffix**: Overwrite existing files; no _v2 or _final.\n");
    fprintf(f, "- **Verifiability**: Action is incomplete until behavioral correctness is confirmed.\n");

    fclose(f);
    printf("🔥 Successfully forged: %s\n", filename);
}

int main(int argc, char *argv[]) {
    if (argc < 5) {
        printf("Usage: %s <title> <problem> <solution> <logic>\n", argv[0]);
        return 1;
    }
    forge_gamma(argv[1], argv[2], argv[3], argv[4]);
    return 0;
}
