#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

/**
 * Problem: Static code definition of GAMMA structures often lacks readability and rigorous PSC headers.
 * Solution: C++ implementation of the GAMMA Forge for high-performance trace generation.
 */
void forge_gamma(std::string title, std::string problem, std::string solution, std::string logic, std::string source = "gemini-cli", std::string target = "any") {
    std::string digest = "This protocol mandates high-fidelity agentic action traces. Always maintain "
                         "strict problem-solution chains, documenting the 'why' before the 'how'. "
                         "Ensure every directive is autonomous, verifiable, and free of version suffixes. "
                         "Map deterministic targets using unified schemas. Execute terminal actions with "
                         "precision, registering every newly generated skill to the central ledger.";

    std::string content = "# GAMMA: " + title + "\n\n" +
                          "**agent-source**: " + source + "\n" +
                          "**agent-target**: " + target + "\n\n" +
                          "## 🤖 For Agents\n" + digest + "\n\n" +
                          "## 1. Problem-Solution Architecture (The 'Why')\n\n" +
                          "**Q: What is the primary bottleneck for this action?**\n" +
                          "**Problem**: " + problem + "\n" +
                          "**Solution**: " + solution + "\n\n" +
                          "## 2. Execution Logic & Finality\n" +
                          "**Logic**: " + logic + "\n\n" +
                          "## 3. Rules & Constraints\n" +
                          "- **Non-Suffix**: Overwrite existing files; no _v2 or _final.\n" +
                          "- **Verifiability**: Action is incomplete until behavioral correctness is confirmed.\n";

    std::string filename = title;
    std::transform(filename.begin(), filename.end(), filename.begin(), ::tolower);
    std::replace(filename.begin(), filename.end(), ' ', '_');
    filename += ".gamma";

    std::ofstream outFile(filename);
    if (outFile.is_open()) {
        outFile << content;
        outFile.close();
        std::cout << "🔥 Successfully forged: " << filename << std::endl;
    } else {
        std::cerr << "❌ Error: Could not create " << filename << std::endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 5) {
        std::cerr << "Usage: " << argv[0] << " <title> <problem> <solution> <logic>" << std::endl;
        return 1;
    }
    forge_gamma(argv[1], argv[2], argv[3], argv[4]);
    return 0;
}
