import unittest
from utils import Utils
from common import eth as eth_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceGasWS(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_maxPriorityFeePerGas_success(self):

        method = f"{self.ns}_maxPriorityFeePerGas"
        result, error = Utils.call_ws(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)
        self.assertEqual(test_data_set["unitGasPrice"], result)

    def test_eth_feeHistory_success(self):

        method = f"{self.ns}_feeHistory"
        params = ["0x10", "latest", [20, 30, 50]]
        result, error = Utils.call_ws(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)


    @staticmethod
    def suite():
        suite = unittest.TestSuite()

        suite.addTest(TestEthNamespaceGasWS("test_eth_maxPriorityFeePerGas_success"))
        suite.addTest(TestEthNamespaceGasWS("test_eth_feeHistory_success"))

        return suite
