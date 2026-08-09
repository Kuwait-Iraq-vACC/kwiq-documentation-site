function aliasApp() {
    return {
        templates: [],
        aliases: [],
        selectedTemplateIndex: -1,
        search: "",
        selectedCategory: "",
        error: "",
        loading: false,

        async init() {
            this.initTheme();
            await this.loadTemplates();
        },

        // --- Theme syncing with MkDocs Material ---
        initTheme() {
            this.syncTheme();

            try {
                const parentHtml = window.parent?.document?.documentElement;
                if (parentHtml && window.parent !== window) {
                    const observer = new MutationObserver(() => this.syncTheme());
                    observer.observe(parentHtml, {
                        attributes: true,
                        attributeFilter: ["data-md-color-scheme"]
                    });
                }
            } catch (e) {
                // Cross-origin parent — can't observe, fall back to OS preference
            }

            const mql = window.matchMedia("(prefers-color-scheme: dark)");
            mql.addEventListener("change", () => {
                if (!this.hasMkDocsParent()) {
                    document.documentElement.classList.toggle("dark", mql.matches);
                }
            });

            window.addEventListener("message", (event) => {
                if (event.data && event.data.mdColorScheme) {
                    this.applySchemeClass(event.data.mdColorScheme);
                }
            });
        },

        hasMkDocsParent() {
            try {
                return !!window.parent?.document?.documentElement?.getAttribute("data-md-color-scheme");
            } catch (e) {
                return false;
            }
        },

        // Pulls the *real* colors MkDocs Material is using on the parent page
        // and copies them into our own CSS variables, so this preview always
        // matches your actual configured theme colors, not a guessed palette.
        syncTheme() {
            let scheme = null;
            let parentStyles = null;

            try {
                const parentHtml = window.parent?.document?.documentElement;
                scheme = parentHtml?.getAttribute("data-md-color-scheme");
                if (parentHtml) {
                    parentStyles = window.parent.getComputedStyle(parentHtml);
                }
            } catch (e) {
                // cross-origin — fall back below
            }

            this.applySchemeClass(scheme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "slate" : "default"));

            if (parentStyles) {
                const vars = {
                    "--bg": "--md-default-bg-color",
                    "--fg": "--md-default-fg-color",
                    "--fg-muted": "--md-default-fg-color--light",
                    "--border": "--md-default-fg-color--lightest",
                    "--input-bg": "--md-code-bg-color"
                };

                for (const [localVar, mdVar] of Object.entries(vars)) {
                    const val = parentStyles.getPropertyValue(mdVar).trim();
                    if (val) {
                        document.documentElement.style.setProperty(localVar, val);
                    }
                }
            }
        },

        applySchemeClass(scheme) {
            document.documentElement.classList.toggle("dark", scheme === "slate");
        },
        // --- end theme syncing ---

        async loadTemplates() {
            this.error = "";
            try {
                const res = await fetch("templates.json");
                if (!res.ok) throw new Error(`templates.json returned ${res.status}`);
                this.templates = await res.json();
            } catch (e) {
                this.error = `Failed to load templates.json: ${e.message}`;
                console.error(e);
            }
        },

        isCategoryHeader(line) {
            return /^;\*{2,}.*\*{2,}\s*$/.test(line.trim());
        },

        extractCategory(line) {
            return line
                .replace(/;/g, "")
                .replace(/\*/g, "")
                .trim()
                .replace(/^\d+\s*/, "");
        },

        async fetchAliases() {
            this.aliases = [];
            this.selectedCategory = "";
            this.error = "";

            if (this.selectedTemplateIndex === -1) return;

            this.loading = true;
            const template = this.templates[this.selectedTemplateIndex];

            try {
                const res = await fetch(template.github_directory_url);
                if (!res.ok) throw new Error(`GitHub directory fetch returned ${res.status}`);
                const files = await res.json();

                for (const file of files) {
                    if (!file.download_url) continue;

                    const fileRes = await fetch(file.download_url);
                    if (!fileRes.ok) {
                        console.warn(`Skipping ${file.name}: ${fileRes.status}`);
                        continue;
                    }
                    const text = await fileRes.text();
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
            } catch (e) {
                this.error = `Failed to load aliases: ${e.message}`;
                console.error(e);
            } finally {
                this.loading = false;
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