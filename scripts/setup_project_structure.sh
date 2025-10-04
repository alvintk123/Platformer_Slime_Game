#!/bin/bash

PROJECT_FOLDER_NAME="" #"PlatformerSlimeGame"

helpFunc()
{
    echo ""
    echo "Usage: $0 [-n name of game project folder]"
    echo ""
    echo "Options: "
    echo " -n  Specify the name of project folder"
    echo " -h  Instruction for use $0"
    echo ""
    echo "Examples"
    echo " $0 -n /PlatformerSlimeGame"
    echo ""
    
}

# Parse options
while getopts "n:h" opt; do
    case $opt in
    n) PROJECT_FOLDER_NAME=$OPTARG ;;
    h)  helpFunc;
        exit 0 ;;

    \?) echo "Invalid option. use -h for help." ; exit 1;;
    esac
done


# Validate PROJECT_FOLDER_NAME provided
if [[ -z "${PROJECT_FOLDER_NAME}" ]]; then
    echo "❌ Error: missing -n <project_folder_name>"
    helpFunc
    exit 1
fi

# Check if valid name folder
if [[ ! "$PROJECT_FOLDER_NAME" =~ ^[a-zA-Z0-9._/-]+$ ]]; then
    echo "❌ Invalid folder name: '$PROJECT_FOLDER_NAME'"
    echo "Only letters, numbers, dot (.), underscore (_), and dash (-), and slash (/) are allowed."
    echo "Invalid option. use -h for help."
    exit 1
fi

# remove leading slash if user accidentally provided it (so it's treated relative to PROJECT_PATH)
PROJECT_FOLDER_NAME="${PROJECT_FOLDER_NAME#/}"

PATH_FOLDER="$PROJECT_PATH/$PROJECT_FOLDER_NAME"

# Check if this folder have already existed
if [ -d "$PATH_FOLDER" ]; then
    echo "'$PATH_FOLDER' have already existed -> lets create project struct."
else
    echo " '$PATH_FOLDER' haven't already existed -> Lets create this project folder."
    echo ""
    # Create root folder
    mkdir -p "$PATH_FOLDER" || {
        echo "❌ Failed to create directory: '$PATH_FOLDER'"
        exit 1
    }

    echo "✅ Folder created at '$PATH_FOLDER'."
fi

cd "$PATH_FOLDER" || {
    echo "❌ Failed to enter directory: '$PATH_FOLDER'"
    exit 1
}

echo "📁 Creating folder structure for $PROJECT_FOLDER_NAME..."

# === ASSETS ===
mkdir -p assets/{sprites/{player/{idle,run,attack,death,jump,hit},enemies/{idle,run,attack,death,hit},items,environment/{tiles,decorations}},backgrounds,audio/{music,sfx},fonts,ui}

# === SOURCE CODE ===
mkdir -p src
touch src/{main.py,player.py,enemy.py,level.py,tilemap.py}

# === LEVELS ===
mkdir -p levels
touch levels

# === DOCUMENTS ===
mkdir -p docs

# === BUILD FOLDER ===
mkdir -p build

# === ROOT FILES ===
touch requirements.txt README.md

echo "✅ Folder structure created successfully!"
