import os

from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.accounts.exceptions import AccountAlreadyExistsError

load_dotenv()


if __name__ == "__main__":
    try:
        QiskitRuntimeService.save_account(
            channel="ibm_quantum", token=os.getenv("QISKIT_IBM_TOKEN")
        )
    except AccountAlreadyExistsError:
        pass
    finally:
        print('Done')