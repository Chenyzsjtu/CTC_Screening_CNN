from dataDirectory import DataDirectory
import os
import data_input
from screen import main
from screen import Test
from model_train import Parameters
from screen_cnn import inference
if __name__ == '__main__':
    dataDirectory = DataDirectory()
    train_dir = os.path.join(dataDirectory.get_current_model_dir(),
                             dataDirectory.checkpoint_fold)
    record_dir = dataDirectory.get_current_record_dir()

    polyp_manager = data_input.Polyp_Manager()
    polyp_manager.read_polyps_from_disk(record_dir, 'all')

    main(train_dir, record_dir, 'all', inference, Parameters)

    #ScreenRatio(checkpoint_dir)+
    Test(polyp_manager, 0.99)
    Test(polyp_manager, 0.9, ifwrite=False)
    Test(polyp_manager, 0.8)
    Test(polyp_manager, 0.6)
    Test(polyp_manager, 0.5)