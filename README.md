# alu-scripting

Projects for the ALU Scripting curriculum.

## API advanced

Python scripts that query the Reddit API: subscriber counts, hot post
titles, recursive pagination and keyword counting.

- Uses the `requests` module with a custom `User-Agent`
- Does not follow redirects (invalid subreddits redirect to search)
- Tasks 2 and 3 query pages recursively (no pagination loops)

### Files

| File | Description |
|------|-------------|
| `api_advanced/0-subs.py` | Number of subscribers for a subreddit |
| `api_advanced/1-top_ten.py` | Titles of the first 10 hot posts |
| `api_advanced/2-recurse.py` | All hot article titles (recursive) |
| `api_advanced/3-count.py` | Keyword counts in hot titles (recursive) |

### Usage

```bash
python3 api_advanced/0-subs.py programming
python3 api_advanced/1-top_ten.py programming
python3 api_advanced/2-recurse.py programming
python3 api_advanced/3-count.py programming 'python java javascript'
```
