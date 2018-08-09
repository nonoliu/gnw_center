include:
  - base.myfun.command.pip
  - base.yunwei.gnw-iptables
gnw-agent-install:
  pip.installed:
    - names: 
      - elasticsearch
      - pymysql
  file.managed:
    - name: /data/app/gnw_agent/agent.py
    - source: salt://base-file/gnw/gnw_agent.py
    - user: dhom
    - group: yw
    - mode: 0644
    - makedirs: True
  cron.present:
    - name: cd /data/app/gnw_agent && python agent.py  >> /data/logs/gnw/gnw.log 2>&1
    - identifier: gnw-agent
    - comment: gnw agent script
    - user: dhom
    - minute: '*/2'
    - require:
      - file: gnw-agent-install
/data/logs/gnw:
  file.directory:
    - user: dhom
    - group: yw
    - mode: 0755
    - makedirs: True
/data/app/gnw_agent/tmp:
  file.directory:
    - user: dhom
    - group: yw
    - mode: 0755
    - makedirs: True
logrotate-gnw-agent:
  file.managed:
    - name: /etc/logrotate.d/gnwagent
    - source: salt://base-file/gnw/agent.logrotate
    - user: root
    - group: root
    - mode: 0644