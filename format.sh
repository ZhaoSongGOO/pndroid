ignores=(
    "./.venv/*"
    "./buildtools/*"
)

find_args=()

for item in "${ignores[@]}"; do
    find_args+=(-not -path "$item")
done

find . -type f -name "*.py" "${find_args[@]}" | xargs black