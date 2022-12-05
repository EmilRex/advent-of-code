if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit 1
fi

path="solutions/$1"

echo "Bootstrapping '${path}'..."

mkdir -p $path
cp template.py $path/code.py
touch $path/example.txt
touch $path/input.txt
code $path/code.py

echo "Done\n"