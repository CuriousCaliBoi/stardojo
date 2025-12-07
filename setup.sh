# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    uv venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies using uv (much faster than pip)
uv pip install -r requirements.txt
cd agent
uv pip install -e .
cd ..
export PYTHONPATH="$PYTHONPATH:$(pwd)/env"
export PYTHONPATH="$PYTHONPATH:$(pwd)"
export PYTHONPATH="$PYTHONPATH:$(pwd)/agent/stardojo"
export PYTHONPATH="$PYTHONPATH:$(pwd)/agent"
cd env