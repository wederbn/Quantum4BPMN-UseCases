FROM camunda/camunda-bpm-platform:run-7.19.0-SNAPSHOT

RUN rm -f /camunda/internal/example/camunda-bpm-run-modules-example-invoice.jar
RUN sed -i "s/camunda.bpm:/camunda.bpm:\n  webapp:\n    header-security:\n       content-security-policy-disabled: true/g" /camunda/configuration/default.yml