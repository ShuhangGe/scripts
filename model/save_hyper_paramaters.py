import logging
import os
#save paramaters 
logging_path = args.log_dir+'/'+'logging'
if not os.path.exists(logging_path):
    os.makedirs(logging_path)
logging.basicConfig(filename=f'{logging_path}/model_paramaters.log', level=logging.INFO)
for arg in vars(args):
    logging.info(f'{arg}: {getattr(args, arg)}')  