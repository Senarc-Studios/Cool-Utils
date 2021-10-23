"""
BSD 3-Clause License

Copyright (c) 2021-present, BenitzCoding
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


# I don't know what to call this, but TextForms sounds like a nice name I guess. It basically gives all forms of text, for example the word "Hello", the following comment will have all it's forms
# HELLO, HELLo, HELlO, HELlo, HElLO, HElLo, HEllO, HEllo, HeLLO, HeLLo, HeLlO, HeLlo, HelLO, HelLo, HellO, Hello, hELLO, hELLo, hELlO, hELlo, hElLO, hElLo, hEllO, hEllo, heLLO, heLLo, heLlO, heLlo, helLO, helLo, hellO, hello
# This took me ages to make lmao

def TextForms(text, sep = None):
    if sep is None:
         sep = ', ' # seperator
    liste = [] # all results
    for x in itertools.product(*zip(text.upper(), text.lower())):
      first = "".join(x) # making words connected
      liste.append(first) # appending words
    final = sep.join(list1) # getting a string with a custom seperator that has all the words
    return final # the final result!
