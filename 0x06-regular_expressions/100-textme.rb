#!/usr/bin/env ruby
sender = ARGV[0].match(/(?<=from:).*?(?=])/)
receiver = ARGV[0].match(/(?<=to:).*?(?=])/)
flags = ARGV[0].match(/(?<=flags:).*?(?=])/)

print(sender)
print(",")
print(receiver)
print(",")
print(flags)

print("\n")
print("\n")
print("\n")
