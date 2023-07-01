"""tests"""
import os
from pathlib import Path

from src.__main__ import load_scripts_from_yamls, write_scripts_to_lua

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

ENV_VARS = {
    'PrgEnv_intel_ver': '1',
    'craype_ver': '2',
    'intel_ver': '3',
    'prod_util_ver': '4',
    'cray_mpich_ver': '5',
    'cray_pals_ver': '6',
    'python_ver': '7',
    'hdf5_ver': '8',
    'crtm_ver': '9',
    'netcdf_ver':'10',
    'prepobs_ver':'11'
}

def test_main(monkeypatch):
    for key, value in ENV_VARS.items():
        monkeypatch.setenv(key, value)
    
    os.environ['prepobs_ver'] = '11'
    print(os.getenv('prepobs_ver'))
    input_path = Path(ROOT_DIR / Path('fixtures/test.yaml'))
    output_path = Path(ROOT_DIR / Path('fixtures/output/'))
    output_path.mkdir(parents=True, exist_ok=True)
        
    script = load_scripts_from_yamls([input_path])
    write_scripts_to_lua(output_path, script)
    assert False
    