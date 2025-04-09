# youtube-transcriptor
A youtube video transcriptor script

## Quick Start

### Ubuntu Install

Setup the virtual env

```bash
python -m venv ./venv
```` 

Then:

```bash
source ./venv/bin/activate
```

**Obs:** To know more about the Venv, check [Venv use example](#Venv-use-example)

Install requirements:

```bash
pip install -r requirements.txt
```

### After install

Example

```bash
echo [video_id] | python ./youtube-transcriptor.py
```

## Note

Is necessary the [`youtube_transcript_api`](https://pypi.org/project/youtube-transcript-api/) module to be installed.
Depending on the local python configuration, the use of virtual env it's recommended.

## Venv use example

To setup the virtual env:

```bash
python -m venv ./venv
```` 

```bash
source ./venv/bin/activate
```

To deactivate, use the `deactivate`.

**NOTE:** This function created by using `source ./venv/bin/activate` (considering the same context of the example)

```bash
deactivate
```

