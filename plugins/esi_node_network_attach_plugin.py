from rally_openstack.task.scenario import scenario
from rally import consts
from rally.task import atomic
from rally.task import validation
import subprocess
import time

@validation.add("required_platform", platform="openstack", users=True)
@scenario.configure(name="ScenarioPlugin.esi_node_network_attach")

class EsiNodeNetworkAttachScenario(scenario.Scenario):
    def esi_node_network_attach(self, node, network, port=None, trunk=None, mac_address=None):
        """Scenario to test 'openstack esi node network attach' command."""
        command = f"openstack esi node network attach --network {network} {node}"
        if port:
            command += f" --port {port}"
        if trunk:
            command += f" --trunk {trunk}"
        if mac_address:
            command += f" --mac-address {mac_address}"

        start_time = time.time()
        output = self._execute_command(command)
        end_time = time.time()
        execution_time = end_time - start_time


    def _execute_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return str(e.output)

    def run(self, node, network, port=None, trunk=None, mac_address=None):
        self.esi_node_network_attach(node, network, port, trunk, mac_address)

