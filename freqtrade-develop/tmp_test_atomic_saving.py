
import os
import shutil
import rapidjson
from pathlib import Path
from unittest.mock import patch, MagicMock

# Importar a classe necessária
from freqtrade.freqai.data_drawer import FreqaiDataDrawer

def test_atomic_saving():
    test_dir = Path("tmp_test_atomic")
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()

    # 1. Criar um arquivo original válido
    pair_dict_path = test_dir / "pair_dictionary.json"
    original_data = {"BTC/USDT": {"model_filename": "old_model"}}
    with open(pair_dict_path, "w") as f:
        rapidjson.dump(original_data, f)

    # Mock da config
    config = {
        "freqai": {
            "identifier": "test_atomic",
            "write_metrics_to_disk": False
        },
        "timeframe": "5m",
        "user_data_dir": Path(".")
    }

    dd = FreqaiDataDrawer(test_dir, config)
    dd.pair_dict = {"BTC/USDT": {"model_filename": "NEW_MODEL"}}

    print("Simulando falha ATÔMICA (interrupção antes do replace)...")
    
    # Vamos simular que o replace falha ou o processo morre antes dele
    with patch.object(Path, 'replace', side_effect=RuntimeError("Crash no sistema!")):
        try:
            dd.save_drawer_to_disk()
        except RuntimeError as e:
            print(f"Erro simulado capturado: {e}")

    # Verificação: O arquivo original NÃO deve ter sido alterado para "NEW_MODEL"
    with open(pair_dict_path, "r") as f:
        current_data = rapidjson.load(f)
    
    print(f"Dados no arquivo original: {current_data}")
    assert current_data == original_data
    print("Sucesso! O arquivo original permaneceu intacto após a falha simulada.")

    # Agora testar o salvamento bem sucedido
    print("\nTestando salvamento atômico com SUCESSO...")
    dd.save_drawer_to_disk()
    
    with open(pair_dict_path, "r") as f:
        final_data = rapidjson.load(f)
    
    print(f"Dados finais no arquivo: {final_data}")
    assert final_data == {"BTC/USDT": {"model_filename": "NEW_MODEL"}}
    print("Sucesso! O arquivo foi atualizado corretamente no fluxo normal.")

    if test_dir.exists():
        shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_atomic_saving()
