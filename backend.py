import notion_df as nd
import pandas as pd
nd.pandas()


notion_token = "secret_omL8nzIdOZySUeAtSOCHm0bUNh2ydXdohuePKPBXkxm"

# Device Database Connection
device_url = "https://www.notion.so/0558f54ce2a34a0ea64e7cfee5ad0d7f?v=d2ba830e965f4f329e74a24c7eaab458&pvs=4"
device_db_id = "0558f54ce2a34a0ea64e7cfee5ad0d7f"
devices_df = pd.DataFrame(nd.download(device_db_id, api_key=notion_token))
devices = devices_df[["Device Label", "Device Type"]]

# Support Ticket Database Connection
tickets_url = "https://www.notion.so/f660a37473f4440cb59fff7356f54d0b?v=99f157fd06874637a59f869ad26802e1&pvs=4"
tickets_db_id = "f660a37473f4440cb59fff7356f54d0b"
tickets = pd.DataFrame(nd.download(tickets_db_id, api_key=notion_token))

# Employee Database Connection
ee_db_id = "03764697bdf74f2b938313815cf62069"
ee_url = "https://www.notion.so/03764697bdf74f2b938313815cf62069?v=e856d446c1a44cfcb8857b014f591284"
ee_df = pd.DataFrame(nd.download(ee_db_id, api_key=notion_token))
ee = ee_df[["Full Name", "EE Code"]][ee_df["Status"]=='Active']