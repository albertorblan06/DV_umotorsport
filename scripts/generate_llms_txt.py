import os
from pathlib import Path


def generate_llms_txt():
    docs_dir = Path("docs")

    if not docs_dir.exists():
        print(f"Directory {docs_dir} does not exist.")
        return

    markdown_files = list(docs_dir.rglob("*.md"))

    # Sort files for deterministic output
    markdown_files.sort()

    llms_full_content = []
    llms_summary_content = []

    llms_summary_content.append("# Documentation Overview\n")
    llms_full_content.append("# Full Documentation\n")

    for file_path in markdown_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

                # Add to summary (just file paths and maybe headings, or just paths)
                relative_path = file_path.relative_to(docs_dir)
                llms_summary_content.append(f"- {relative_path}")

                # Add to full content
                llms_full_content.append(f"## File: {relative_path}\n")
                llms_full_content.append(content)
                llms_full_content.append("\n" + "=" * 40 + "\n")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(llms_summary_content))

    with open("llms-full.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(llms_full_content))

    print("Generated llms.txt and llms-full.txt")


if __name__ == "__main__":
    generate_llms_txt()
