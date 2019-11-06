# Caldex
Caldex (Caldera Export) is a [Caldera](https://github.com/mitre/caldera) plugin generating a [MITRE ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) layer outlining successful and failed technique mitigations.

## Installation

Installing Caldex assumes basic knowledge of [Plugins within Caldera](https://github.com/mitre/caldera/wiki/What-is-a-plugin).

As one would do for any Caldera plugin, installing Caldex can be achieved using the following operations:

1. Clone Caldex into Caldera's `plugin` folder using one of the [supported versions](https://github.com/NVISO-BE/caldex/releases) (i.e. `2.3.2`).

   ```bash
   # This command assumes "~/caldera" to be Caldera's root.
   # You might need to change this accordingly (i.e. "/home/user/Downloads/caldera").
   git clone -C ~/caldera/plugins -b "2.3.2" https://github.com/NVISO-BE/caldex.git
   ```

2. Add Caldex to the enabled plugins in the used Caldera configuration file (i.e. `~/caldera/conf/local.yml`). The following snippet is an example using the default configuration.

   ```yaml
   ---
   
   host: 0.0.0.0
   port: 8888
   exfil_dir: /tmp
   memory: True
   untrusted_timer: 180
   plugins:
     - stockpile
     - sandcat
     - gui
     - chain
     - caldex # Insert "caldex" into the list of used plugins.
   debug: False
   users:
     admin: admin
   ```

3. Restart Caldera to apply the configuration changes.