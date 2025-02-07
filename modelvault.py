import os
import json
import pickle
from pathlib import Path
from typing import Any, Dict, List, Optional


class ModelVault:
    """
    A simple file‑system based model registry.
    Models are stored as pickled objects alongside a JSON metadata file.
    """

    def __init__(self, base_dir: str):
        """
        Initialise the vault.

        Args:
            base_dir: Directory where all models will be stored.
        """
        self.base_path = Path(base_dir).expanduser().resolve()
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _model_dir(self, name: str) -> Path:
        """Return the directory for a given model name."""
        return self.base_path / name

    def _metadata_path(self, name: str, version: int) -> Path:
        """Path to the metadata file for a specific version."""
        return self._model_dir(name) / f"v{version}_meta.json"

    def _model_path(self, name: str, version: int) -> Path:
        """Path to the pickled model for a specific version."""
        return self._model_dir(name) / f"v{version}_model.pkl"

    def _next_version(self, name: str) -> int:
        """Determine the next version number for a model."""
        versions = self.list_versions(name)
        return max(versions) + 1 if versions else 1

    def save(self, name: str, model: Any, metadata: Optional[Dict] = None) -> int:
        """
        Save a model with optional metadata.

        Returns:
            The version number assigned to the saved model.
        """
        version = self._next_version(name)
        model_dir = self._model_dir(name)
        model_dir.mkdir(parents=True, exist_ok=True)

        # Serialize model
        model_path = self._model_path(name, version)
        with open(model_path, "wb") as f:
            pickle.dump(model, f)

        # Store metadata
        meta = metadata or {}
        meta.update({"version": version})
        meta_path = self._metadata_path(name, version)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

        return version

    def load(self, name: str, version: int) -> Any:
        """
        Load a specific version of a model.

        Raises:
            FileNotFoundError if the requested version does not exist.
        """
        model_path = self._model_path(name, version)
        if not model_path.is_file():
            raise FileNotFoundError(f"Model {name} version {version} not found.")
        with open(model_path, "rb") as f:
            return pickle.load(f)

    def load_latest(self, name: str) -> Any:
        """Load the most recent version of a model."""
        versions = self.list_versions(name)
        if not versions:
            raise FileNotFoundError(f"No versions found for model {name}.")
        return self.load(name, max(versions))

    def list_versions(self, name: str) -> List[int]:
        """
        List all saved versions for a model, sorted ascending.
        """
        model_dir = self._model_dir(name)
        if not model_dir.is_dir():
            return []
        versions = []
        for file in model_dir.iterdir():
            if file.suffix == ".pkl" and file.stem.startswith("v"):
                try:
                    v = int(file.stem.split("_")[0][1:])
                    versions.append(v)
                except ValueError:
                    continue
        return sorted(versions)

    def get_metadata(self, name: str, version: int) -> Dict:
        """
        Retrieve metadata for a specific model version.

        Returns an empty dict if metadata is missing.
        """
        meta_path = self._metadata_path(name, version)
        if not meta_path.is_file():
            return {}
        with open(meta_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete_version(self, name: str, version: int) -> None:
        """
        Remove a specific version of a model and its metadata.
        """
        model_path = self._model_path(name, version)
        meta_path = self._metadata_path(name, version)
        for p in (model_path, meta_path):
            try:
                p.unlink()
            except FileNotFoundError:
                pass
        # Clean up model directory if empty
        model_dir = self._model_dir(name)
        if not any(model_dir.iterdir()):
            model_dir.rmdir()


class _MF01:
    version = 2


class _MK7l:
    version = 3


class _MByi:
    version = 4

# TODO: revisit logic (aokd2)


class _MMwg:
    version = 6


class _MZsi:
    version = 7


def _helper_twi8q(x):
    # step 8
    return x + 8

# TODO: revisit logic (wq84f)


class _MUbp:
    version = 10

# TODO: revisit logic (ulxbt)


def _helper_pcsk0(x):
    # step 12
    return x + 12


class _MEz3:
    version = 13


def _helper_quzy4(x):
    # step 14
    return x + 14


class _MDmp:
    version = 15


class _M10i:
    version = 16


def _helper_cvwcj(x):
    # step 17
    return x + 17


def _helper_xq9di(x):
    # step 18
    return x + 18


def _helper_4rjmg(x):
    # step 19
    return x + 19


class _MV5f:
    version = 20


class _MHow:
    version = 21

# TODO: revisit logic (w0psp)
