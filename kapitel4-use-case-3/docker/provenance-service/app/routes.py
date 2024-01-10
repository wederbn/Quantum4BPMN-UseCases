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
from app import app, unfolding_utils
from flask import jsonify, abort, request


@app.route('/provenance-service', methods=['POST'])
def mitigate_error():
    """Mitigate the readout-error from the given result distribution."""

    app.logger.info('Received Post request to mitigate error...')
    if not request.json:
        app.logger.error("Service currently only supports JSON")
        abort(400, "Only Json supported")

    if 'QPU' not in request.json:
        app.logger.error("QPU not defined in request")
        abort(400, "QPU not defined in request")
    qpu = request.json['QPU']

    if 'UnfoldingTechnique' not in request.json:
        app.logger.error("UnfoldingTechnique not defined in request")
        abort(400, "UnfoldingTechnique defined in request")
    unfolding_technique = request.json['UnfoldingTechnique']
    if not unfolding_technique == 'fullMatrix':
        app.logger.error("UnfoldingTechnique is not supported. Currently only Correction Matrix can be used")
        abort(400, "UnfoldingTechnique is not supported. Currently only Correction Matrix can be used")

    max_age = request.json['MaxAge']

    access_token = request.json['AccessToken']

    if 'Result' not in request.json:
        app.logger.error("Result not defined in request")
        abort(400, "Result not defined in request")
    result = request.json['Result']
    app.logger.info("Result to mitigate: " + result)

    app.logger.info("Passed input is valid")

    return jsonify({'Result': unfolding_utils.mitigate_error(qpu, max_age, result, access_token)}), 200
