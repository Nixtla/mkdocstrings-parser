devenv:
	uv sync --all-extras --quiet --dev --frozen
	uv pip install -e .
	uv run pre-commit install

licenses:
	pip-licenses --format=csv --with-authors --with-urls > third_party_licenses.csv
	python scripts/filter_licenses.py
	rm -f third_party_licenses.csv
	@echo "✓ THIRD_PARTY_LICENSES.md updated"
