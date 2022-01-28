# `hof`

Not practical tool to make Baseball Hall of Fame as you want.

## Usage

```bash
$ hof
Usage: hof [OPTIONS] COMMAND [ARGS]...

  root command.

Options:
  --help  Show this message and exit.

Commands:
  add      add someone to hof.
  destroy  destroy hof.
  init     initialize hof data.
  remove   remove someone from hof.
  show     show hof data.

$ how init
Done! ✨

$ hof show --head 5
┏━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ YEAR ┃ VOTEDBY ┃ BALLOTS ┃ NEEDED ┃ VOTES ┃ INDUCTED ┃ CATEGORY ┃ NAME              ┃
┡━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ 1936 │ BBWAA   │ 226.0   │ 170.0  │ 222.0 │ Y        │ Player   │ Ty Cobb           │
│ 1936 │ BBWAA   │ 226.0   │ 170.0  │ 215.0 │ Y        │ Player   │ Babe Ruth         │
│ 1936 │ BBWAA   │ 226.0   │ 170.0  │ 215.0 │ Y        │ Player   │ Honus Wagner      │
│ 1936 │ BBWAA   │ 226.0   │ 170.0  │ 205.0 │ Y        │ Player   │ Christy Mathewson │
│ 1936 │ BBWAA   │ 226.0   │ 170.0  │ 189.0 │ Y        │ Player   │ Walter Johnson    │
└──────┴─────────┴─────────┴────────┴───────┴──────────┴──────────┴───────────────────┘

$ hof remove --name "ty cobb"
Removed! 💀
ty cobb is no longer on hof..

$ hof destroy
Done! 💣
Goodbye baseball.. ✋
┏━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━┓
┃ YEAR ┃ VOTEDBY ┃ BALLOTS ┃ NEEDED ┃ VOTES ┃ INDUCTED ┃ CATEGORY ┃ NAME ┃
┡━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━┩
└──────┴─────────┴─────────┴────────┴───────┴──────────┴──────────┴──────┘
```