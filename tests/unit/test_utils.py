import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path 
from box import ConfigBox 
from ensure.main import EnsureError

yaml_file = [
    "tests/data/demo.yaml",
    "tests/data/empty.yaml",
]

def test_read_yaml_empty():
    with pytest.raises(ValueError):
        read_yaml(Path(yaml_file[0]))
        

def test_read_yaml_return_type():
    respone = read_yaml(Path(yaml_file[-1]))
    assert isinstance(respone, ConfigBox)
   
   
@pytest.mark.parametrize("path_to_yaml",yaml_file) 
def test_read_yaml_bad_type(path_to_yaml):
    with pytest.raises(EnsureError):
        read_yaml(path_to_yaml)
        

class Test_read_yaml:
    yaml_file = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml",
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_file[0]))
            
    def test_read_yaml_return_type(self):
        respone = read_yaml(Path(self.yaml_file[-1]))
        assert isinstance(respone, ConfigBox)
      
    @pytest.mark.parametrize("path_to_yaml",yaml_file) 
    def test_read_yaml_bad_type(self, path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)
        
    
        
        