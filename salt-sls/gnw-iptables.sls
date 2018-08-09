gnw-agent-iptables:
  file.append:
    - name: /data/tools/iptables/user.rule
    - text: -A OUTPUT -p tcp --dport 80 -j ACCEPT
  cmd.run:
    - name: bash /data/tools/iptables/iptables.sh
    - require:
      - file: gnw-agent-iptables