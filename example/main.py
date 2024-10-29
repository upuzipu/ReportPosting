from src.client.result_client import ResultPostingClient

RPC = ResultPostingClient()

data = RPC.put_data_in_report("1Nwc84JbeQtKfMDDsyrh1k_tiG5hvju-mmadN9uNsQoU",
                              "1omRSaYjAc0Dy4l7XQT7WoIWlyfVzRsaQE2Uw0CNlB8Q")
RPC.put_data_in_admin(2034, "HEARTHSTONE", data, "2024-10-26")
