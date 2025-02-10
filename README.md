# youtube-transcriptor
A youtube video transcriptor script

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

> [!NOTE] This function created by using `source ./venv/bin/activate` (considering the same context of the example)

```bash
deactivate
```

## Use sample

```bash
echo [video_id] | python ./youtube-transcriptor.py
```

