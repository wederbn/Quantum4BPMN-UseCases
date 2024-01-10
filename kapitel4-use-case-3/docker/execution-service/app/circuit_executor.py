# ******************************************************************************
#  Copyright (c) 2020 University of Stuttgart
#
#  See the NOTICE file(s) distributed with this work for additional
#  information regarding copyright ownership.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ******************************************************************************
import time

from qiskit import QuantumCircuit, IBMQ, transpile, assemble
from qiskit.providers import QiskitBackendNotFoundError, JobError, JobTimeoutError
from qiskit.providers.ibmq.api.exceptions import RequestsApiError
from qiskit.providers.jobstatus import JOB_FINAL_STATES

from app import app


def execute_circuit(quantum_circuit, qpu, access_token, shots):
    """Execute the given circuit on the given quantum computer"""

    # get qiskit circuit object from OpenQASM string
    circuit = QuantumCircuit.from_qasm_str(quantum_circuit)
    app.logger.info("Loaded circuit for execution:")
    app.logger.info(circuit)

    ibm_qpu = get_qpu(access_token, qpu)
    if ibm_qpu is None:
        app.logger.error("Unable to retrieve qpu object with given name and given access token")
        return "Unable to load account with given access token."
    transpiled_circuit = transpile(circuit, backend=ibm_qpu)

    app.logger.info(
        "Start executing transpiled circuit with width " + str(transpiled_circuit.num_qubits) + " and depth " + str(
            transpiled_circuit.depth()))
    result_counts = execute(transpiled_circuit, shots, ibm_qpu)
    if result_counts is None:
        app.logger.error("Execution failed!")
        return "Execution failed!"
    app.logger.info("Execution returned the following result counts: " + str(result_counts))

    return str(result_counts)


def get_qpu(access_token, qpu):
    """Load account from token. Get backend."""
    try:
        IBMQ.save_account(access_token, overwrite=True)
        IBMQ.load_account()
        provider = IBMQ.get_provider(group='open')
        backend = provider.get_backend(qpu)
        app.logger.info("QPU object successfully retrived from IBMQ")
        return backend
    except (QiskitBackendNotFoundError, RequestsApiError):
        return None


def execute(transpiled_circuit, shots, backend):
    """Execute the quantum circuit."""
    try:
        job = backend.run(assemble(transpiled_circuit, shots=shots))

        job_status = job.status()
        while job_status not in JOB_FINAL_STATES:
            app.logger.info("The execution is still running")
            time.sleep(20)
            job_status = job.status()

        return job.result().get_counts()
    except (JobError, JobTimeoutError):
        return None
