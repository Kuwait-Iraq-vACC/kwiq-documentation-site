function aliasApp() {
    return {
        templates: [],
        aliases: [],
        selectedTemplateIndex: -1,
        search: "",
        selectedCategory: "",

        async init() {
            await this.loadTemplates();
        },

        async loadTemplates() {
            const res = await fetch("templates.json");
            this.templates = await res.json();
        },

        // Matches lines like ";*** ** APPROACH ** ***" or ";*** 1 Logging on ***"
        isCategoryHeader(line) {
            return /^;\*{2,}.*\*{2,}\s*$/.test(line.trim());
        },

        extractCategory(line) {
            return line
                .replace(/;/g, "")
                .replace(/\*/g, "")
                .trim()
                .replace(/^\d+\s*/, ""); // strip leading numbering like "1 "
        },

        async fetchAliases() {
            this.aliases = [];
            this.selectedCategory = "";

            if (this.selectedTemplateIndex === -1) return;

            const template = this.templates[this.selectedTemplateIndex];

            const res = await fetch(template.github_directory_url);
            const files = await res.json();

            for (const file of files) {
                if (!file.download_url) continue;

                const text = await fetch(file.download_url).then(r => r.text());
                const lines = text.split("\n");

                let currentCategory = "General";

                for (const rawLine of lines) {
                    const line = rawLine.trim();

                    if (this.isCategoryHeader(line)) {
                        currentCategory = this.extractCategory(line);
                        continue;
                    }

                    if (!line.startsWith(".")) continue;

                    const parts = line.split(" ");
                    const alias = parts[0];
                    const text = parts.slice(1).join(" ");

                    this.aliases.push({
                        category: currentCategory,
                        alias,
                        text
                    });
                }
            }
        },

        get categories() {
            return [...new Set(this.aliases.map(a => a.category))].sort();
        },

        get filteredAliases() {
            let result = this.aliases;

            if (this.selectedCategory) {
                result = result.filter(a => a.category === this.selectedCategory);
            }

            if (this.search) {
                const s = this.search.toLowerCase();
                result = result.filter(a =>
                    a.alias.toLowerCase().includes(s) ||
                    a.text.toLowerCase().includes(s)
                );
            }

            return result;
        }
    };
}