from pathlib import Path

from allaystone import Plugin


class TemplatePlugin(Plugin):
    version = "0.1.0"
    api_version = "0.27.0"
    description = "Template Python plugin for AllayStone."
    authors = ["Your Name"]
    website = "https://github.com/smartcmd/AllayStoneTemplate"

    def on_load(self):
        self.logger.info("TemplatePlugin loaded.")

    def on_enable(self):
        data_folder = Path(self.data_folder)
        data_folder.mkdir(parents=True, exist_ok=True)
        marker = data_folder / "template.txt"
        marker.write_text(
            "Hello from the AllayStone template.\n"
            f"name={self.name}\n"
            f"version={self.version}\n",
            encoding="utf-8",
        )
        self.logger.info("TemplatePlugin enabled. Wrote " + str(marker))

    def on_disable(self):
        self.logger.info("TemplatePlugin disabled.")
