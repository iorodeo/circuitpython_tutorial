for entry in *
do
    case $entry in 
        *.py)
            echo $entry "->" /media/$USER/CIRCUITPY
            cp $entry /media/$USER/CIRCUITPY
            ;;
    esac
done
sync
