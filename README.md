# Memory consumption per process

Script simples que tem como objetivo verificar o consumo de memória dos processos.

Alterar a variável "file = open(home_dir + "/scripts/.Config", "r")" para o caminho onde encontra-se seu arquivo de configuração contendo os nomes dos processos que deseja-se monitorar:

Ex.:
```console
cat .Config

logstash
metricbeat
elasticsearch
kibana
```
Para executar:
```console
./check_process.py

====================================================================================================
                                      Process Status                                      
====================================================================================================
PROCESS: logstash              PID: 19133    MEMORY % : 18.59     STARTED: 2020-06-11 15:49:34
PROCESS: metricbeat            PID: 65954    MEMORY % : 0.06      STARTED: 2020-05-26 17:20:14
PROCESS: elasticsearch         PID: 11989    MEMORY % : 40.73     STARTED: 2020-05-03 23:00:04
PROCESS: kibana                PID: 109232   MEMORY % : 0.55      STARTED: 2020-06-18 15:56:20

```