import sys


def format_line(index_and_comment):
	index, comment = index_and_comment
	return "Line {}: {}".format(index, comment.lstrip('#').strip())


lines_wo_spaces = map(str.lstrip, sys.stdin)
comment_lines = filter(lambda index_line: index_line[1].startswith('#'), enumerate(lines_wo_spaces, 1))
numerated_comments = map(format_line, comment_lines)
print(*numerated_comments, sep='\n')
