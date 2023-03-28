#!/usr/bin/env ruby
ARGV[0].scan(/\bh[a-z0-9A-Z]n\b$/).each do |i|
  print i
  STDOUT.flush
end
print("\n")
