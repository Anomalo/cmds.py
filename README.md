# cmds.py
Takes as input a .cmd file and prints out a the command in it in a format that can be used in bash
it can be used as
  python cmds.py kraken.cmd

if no file is given as an argument then it will proceed to read all the .cmd files.

basic cmd file format:
##title
command
  -options
  -tabs can be used freely to organise command options

##double hash separates commands and indicates te title
another command
  its options


sample .cmd:
#########################################################################################################
##kraken organise step
/nfs/research2/enright/hsaini/seqimp-13-274/bin/command_imp.pl
        --step=organise
        --description=description.txt
        --user-configuration=config.txt
        --paired
        --dataDir=raw_files
        --no-unique

##kraken reaper step
bsub -q research-rh6 -n 9 -M 6000 -R'rusage[mem=6000:tmp=12000]' -o logs/reaper.log -e logs/reaper.err
        "
        /nfs/research2/enright/hsaini/seqimp-13-274/bin/imp_commandline.pl
                --step=reaper
                --description=description.txt
                --user-configuration=config.txt
                --paired
                --analysisDir=analysis
                --dataDir=raw_files
                --processors=9  #has to match
        "

##kraken filter step
bsub -q research-rh6 -n 9 -M 60000 -R'rusage[mem=60000:tmp=12000]' -o logs/filter.log -e logs/filter.err
        "
        /nfs/research2/enright/hsaini/seqimp-13-274/bin/command_imp.pl
                --step=filter
                --description=description.txt
                --user-configuration=config.txt
                --paired
                --dataDir=analysis
                --no-unique
                --processors=9
        "
#########################################################################################################

Tabs are ignored, as well as things on the right of # comments. 
The command separator is a double hash ##.
text next to the ## will be considered the title of the command.

That sample file would have outputed:
#########################################################################################################
kraken.cmd
kraken organise step
/nfs/research2/enright/hsaini/seqimp-13-274/bin/command_imp.pl --step=organise --description=description.txt--user-configuration=config.txt--paired--dataDir=raw_files--no-unique


kraken reaper step
bsub -q research-rh6 -n 9 -M 6000 -R'rusage[mem=6000:tmp=12000]' -o logs/reaper.log -e logs/reaper.err "/nfs/research2/enright/hsaini/seqimp-13-274/bin/imp_commandline.pl  --step=reaper  --description=description.txt --user-configuration=config.txt --paired --analysisDir=analysis --dataDir=raw_files --processors=9"


kraken filter step
bsub -q research-rh6 -n 9 -M 60000 -R'rusage[mem=60000:tmp=12000]' -o logs/filter.log -e logs/filter.err "/nfs/research2/enright/hsaini/seqimp-13-274/bin/command_imp.pl --step=filter --description=description.txt--user-configuration=config.txt--paired--dataDir=analysis--no-unique--processors=9"
#########################################################################################################
this can then be placed in a file by:
python cmds.py > commands.txt


