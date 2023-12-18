# usage in terminal: ./deploy.sh | ./deploy.sh all | ./deploy.sh model | ./deploy.sh web
# default arg: all

#receives arg from terminal, ex: ./deploy.sh model, arg = "model"
arg="$1" 

if [ -z $arg ]; then
  arg="all"
fi

if [ "$arg" == "help" ]; then
  echo "usage: ./deploy.sh | ./deploy.sh all | ./deploy.sh model | ./deploy.sh web"
  echo "default arg: all"
fi

if [ "$arg" == "all" ] || [ "$arg" == "model" ]; then
  python3 -m venv env &&
  source env/bin/activate
  source env/Scripts/activate
  pip3 install -r RnD/requirements.txt &&
  python3 RnD/model-build.py
fi

if [ "$arg" == "all" ] || [ "$arg" == "web" ]; then
  python3 -m venv env &&
  source env/bin/activate
  source env/Scripts/activate
  pip3 install -r web-server/requirements.txt &&
  python3 web-server/server.py
fi

if [ $arg != "all" ] && [ $arg != "model" ] && [ $arg != "web" ] && [ $arg != "help" ]; then
  echo "Invalid arg $arg"
  echo "usage: ./deploy.sh | ./deploy.sh all | ./deploy.sh model | ./deploy.sh web"
  echo "default arg: all"
fi


