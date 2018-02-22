APP_ROOT=$(dirname)

UNAMEOUT="$(uname -s)"

case "${UNAMEOUT}" in
    Linux*)             MACHINE=linux;;
    Darwin*)            MACHINE=mac;;
    *)                  MACHINE="UNKNOWN"
esac

if [ "$MACHINE" == "UNKNOWN" ]; then
    echo "Unsupported system type"
    echo "System must be a Macintosh, Linux or Windows"
    echo ""
    echo "System detection determined via uname command"
    echo "If the following is empty, could not find uname command: $(which uname)"
    echo "Your reported uname is: $(uname -s)"
fi

if [ "$MACHINE" == "linux" ]; then
    if grep -q Microsoft /proc/version; then # WSL
        export XDEBUG_HOST=10.0.75.1
    else
        if [ "$(command -v ip)" ]; then
            export XDEBUG_HOST=$(ip addr show docker0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
        else
            export XDEBUG_HOST=$(ifconfig docker0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1)
        fi
    fi
    SEDCMD="sed -i"
elif [ "$MACHINE" == "mac" ]; then
    export XDEBUG_HOST=$(ipconfig getifaddr en0)

    if [ -z "$XDEBUG_HOST" ]; then
        export XDEBUG_HOST=$(ipconfig getifaddr en1)
    fi
    SEDCMD="sed -i .bak"
fi

export APP_PORT=${APP_PORT:-80}
export WWWUSER=$(whoami)

if [ ! -f .env ]; then
    cp .env.dist .env
fi

echo "Building the container"

docker-compose -p ccqc -f docker-compose.yml up -d --build

echo ""
echo "Complete!"