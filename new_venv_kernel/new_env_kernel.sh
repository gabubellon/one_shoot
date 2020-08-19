#!bash

while getopts v: OPT; do
case $OPT in
"v") VENV=${OPTARG};;
esac
done

## CHANGE TO YOUR LOCAL VIRTUAL ENV STORAGE
VENVS="$HOME/.virtualenvs/"

if [ -z "$VENV" ];
  then 
    echo "Virtualenv name not provide on -v parameter";
  else

    VENVDIR="$VENVS/$VENV/bin/"
    
    if [[ ! -d $VENVDIR ]]; 
        then
	        echo "Virtualenv not exists"
        else 

            echo ""
            echo "####"
            echo "#### Source to env $VENV #####"
            echo "####"
            echo ""

            source $VENVDIR/activate

            echo ""
            echo "####"
            echo "#### Installing ipython and ipykernel ####"
            echo "####"
            echo ""
            pip install ipython ipykernel

            echo ""
            echo "####"
            echo "#### Creating kernel instance ####"
            echo "####"
            echo ""
            ipython kernel install --user --name ${VENV}

            echo ""
            echo "####"
            echo "#### Deactivate to env $VENV" 
            echo "####"
            echo ""
            source deactivate

            echo "#### $VENV added to jupyter ####"
    fi
fi
