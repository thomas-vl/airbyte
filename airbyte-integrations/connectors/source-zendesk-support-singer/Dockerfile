FROM airbyte/integration-base-singer:dev

RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

ENV CODE_PATH="source_zendesk_support_singer"
ENV AIRBYTE_IMPL_MODULE="source_zendesk_support_singer"
ENV AIRBYTE_IMPL_PATH="SourceZendeskSupportSinger"

WORKDIR /airbyte/integration_code
COPY $CODE_PATH ./$CODE_PATH
COPY setup.py ./
RUN pip install ".[main]"

LABEL io.airbyte.version=0.1.1
LABEL io.airbyte.name=airbyte/source-zendesk-support-singer
