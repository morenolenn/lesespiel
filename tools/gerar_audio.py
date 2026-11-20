import asyncio, json, re, os, sys
import edge_tts
src, outdir = sys.argv[1], sys.argv[2]
html = open(src, encoding='utf-8').read()
words = json.loads(re.search(r'<script id="words" type="application/json">(.*?)</script>', html, re.S).group(1))['words']
words += json.loads(re.search(r'<script id="sentences" type="application/json">(.*?)</script>', html, re.S).group(1))['sentences']
VOICES = {
  'tanja':     ('de-DE-TanjaNeural', 'de', 'Hallo Lara! Super gemacht!'),
  'ingrid':    ('de-AT-IngridNeural', 'de', 'Hallo Lara! Super gemacht!'),
  'christoph': ('de-DE-ChristophNeural', 'de', 'Hallo Lara! Super gemacht!'),
  'francisca': ('pt-BR-FranciscaNeural', 'pt', 'Oi Lara! Muito bem!'),
}
sem = asyncio.Semaphore(6)
async def one(voice, text, path):
  if os.path.exists(path) and os.path.getsize(path) > 500: return 0
  async with sem:
    for attempt in range(4):
      try:
        await edge_tts.Communicate(text, voice, rate='-10%').save(path); return 1
      except Exception as e:
        await asyncio.sleep(1.5 * (attempt + 1))
  print('FAIL', voice, text); return 0
async def main():
  jobs = []
  for key, (voice, lang, hello) in VOICES.items():
    d = os.path.join(outdir, key); os.makedirs(d, exist_ok=True)
    jobs.append(one(voice, hello, os.path.join(d, '_hallo.mp3')))
    for w in words:
      jobs.append(one(voice, (w[lang] if w[lang].endswith(('.', '!', '?')) else w[lang] + '.'), os.path.join(d, w['id'] + '.mp3')))
  n = sum(await asyncio.gather(*jobs)); print('generated', n, 'of', len(jobs))
asyncio.run(main())
