import yaml
from multi_document_rag.utils.paths import LOG_DIR
import os

class Config:
    def __init__(self, title=None, path=os.path.join(LOG_DIR, "config", "config.yaml")):
        self.title = title
        with open(path, "r") as f:
            self.cfg = yaml.safe_load(f)
            
    def __getitem__(self, item):
        section = self.title if self.title else item
        return self.cfg[item]

if __name__ == "__main__":
    config = Config()
    print(config.cfg)