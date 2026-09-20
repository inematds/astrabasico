#!/usr/bin/env python3
"""Estimate one API request using explicit, dated rates. No network or credentials."""
import argparse
import json
from decimal import Decimal
from pathlib import Path

def estimate(total, cached, written, output, pricing):
    values=(total,cached,written,output)
    if any(x<0 for x in values):
        raise ValueError('Contagens não podem ser negativas.')
    if cached+written>total:
        raise ValueError('Cache lido + escrito não pode superar a entrada total.')
    rates=pricing['per_million']; long=pricing['long_context']
    if any(Decimal(str(rates[k]))<0 for k in ('input','cached','cache_write','output')):
        raise ValueError('Tarifas não podem ser negativas.')
    is_long=total>long['above_input_tokens']
    im=Decimal(str(long['input_multiplier'])) if is_long else Decimal(1)
    om=Decimal(str(long['output_multiplier'])) if is_long else Decimal(1)
    parts={k:Decimal(n)*Decimal(str(rates[k]))*m/Decimal(1000000) for k,n,m in (
        ('input',total-cached-written,im),('cached',cached,im),('cache_write',written,im),('output',output,om))}
    return {'estimated':True,'product':pricing['product'],'model':pricing['model'],
        'rates_checked_at':pricing['checked_at'],'long_context':is_long,
        'breakdown_usd':{k:float(v) for k,v in parts.items()},'total_usd':float(sum(parts.values())),
        'source':pricing['source'],'limitations':pricing['notes']}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=int,required=True,help='Total input tokens, including cached and cache writes')
    p.add_argument('--cached',type=int,default=0)
    p.add_argument('--cache-write',type=int,default=0)
    p.add_argument('--output',type=int,required=True,help='All billable output tokens, including reasoning when billed')
    p.add_argument('--pricing',type=Path,default=Path(__file__).resolve().parents[1]/'references/precos.json')
    a=p.parse_args()
    try: result=estimate(a.input,a.cached,a.cache_write,a.output,json.loads(a.pricing.read_text()))
    except (ValueError,KeyError,OSError) as e:p.error(str(e))
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
