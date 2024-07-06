from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from ntc_templates.parse import parse_output, ParsingException
from pprint import pprint

nornir_init_object = InitNornir(config_file="network-configuration-parser/config/config.yaml")

user_command = 'show clock'

results = nornir_init_object.run(task = netmiko_send_command, command_string=user_command)

final_results = []

for hostname, result in results.items():
    if result.failed is False:
        # print(hostname)
        # print(result[0].result)
        #print(result[0].host.platform)
        try:
            version_parsed = parse_output(platform=result[0].host.platform, command=user_command, data=result[0].result)
        except ParsingException:
            version_parsed = None
        # print(version_parsed)
        final_results.append(
            {
                "hostname" : hostname,
                "command": user_command,
                "raw_output":result[0].result,
                "pasred_output": version_parsed
            }
        )
pprint(final_results)




 



# I need a simply inventory to use
# I Need to connect to a device
# I need to run a show command
# I need to output to screen

## I want the ability for users to create their own templates in their own folder
