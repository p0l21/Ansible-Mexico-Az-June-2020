#!/bin/bash
# import variables from ansible
source $1
#state=${state:-}
if [[ $state == "happy" ]]; then
        echo "happy" > $file
        echo { \"changed\": true }
fi

if [[ $state == "sad" ]]; then
	if [ -e $file ]; then
		rm $file
		echo { \"changed\": true }
		exit 0
	else
		echo { \"changed\": false}
		exit 0
	fi
fi
