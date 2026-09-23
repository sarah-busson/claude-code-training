"""Stage 1 profile: Load, clean, explore. Build 12-figure visual tour."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = '#f8f9fa'

# Load & clean
market = pd.read_csv('data/raw/Staten_Island_housing_market_case.csv')
portfolio = pd.read_csv('data/raw/portfolio.csv')

market = market.dropna(subset=['price'])
market['sale_date'] = pd.to_datetime(market['sale_date'])

print(f"Market: {len(market):,} transactions")
print(f"Portfolio: {len(portfolio):,} homes")

# === Tour ===
figs_created = 0

# Fig 1: Price distribution
fig, ax = plt.subplots(figsize=(11, 6))
ax.hist(market['price'], bins=60, color='steelblue', edgecolor='black', alpha=0.7)
ax.axvline(market['price'].median(), color='red', linestyle='--', linewidth=2.5, label=f"Median: ${market['price'].median():,.0f}")
ax.set_xlabel('Sale Price ($)', fontsize=11, fontweight='bold')
ax.set_ylabel('Count', fontsize=11, fontweight='bold')
ax.set_title('Figure 1: Market Price Distribution (Highly Skewed)', fontsize=12, fontweight='bold')
ax.set_xlim(0, 1200000)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.savefig('outputs/figures/01_tour_01_price_dist.png', dpi=150, bbox_inches='tight')
plt.close()
figs_created += 1

# Fig 2: Price trend
fig, ax = plt.subplots(figsize=(12, 6))
yearly = market.groupby('year')['price'].median()
ax.plot(yearly.index, yearly.values, marker='o', linewidth=3, markersize=10, color='darkgreen')
ax.fill_between(yearly.index, yearly.values * 0.9, yearly.values * 1.1, alpha=0.2, color='green')
ax.axvline(2008, color='red', linestyle=':', linewidth=2, alpha=0.7)
ax.axvline(2012, color='orange', linestyle=':', linewidth=2, alpha=0.7)
ax.set_xlabel('Year', fontsize=11, fontweight='bold')
ax.set_ylabel('Median Price ($)', fontsize=11, fontweight='bold')
ax.set_title('Figure 2: Market Price Trend 2003–2013', fontsize=12, fontweight='bold')
ax.grid(alpha=0.3)
plt.savefig('outputs/figures/01_tour_02_price_trend.png', dpi=150, bbox_inches='tight')
plt.close()
figs_created += 1

# Fig 3: Top neighborhoods
fig, ax = plt.subplots(figsize=(10, 6))
top_nbhd = market.groupby('nbhd')['price'].median().sort_values(ascending=False).head(12)
top_nbhd.plot(kind='barh', ax=ax, color='coral', edgecolor='black', alpha=0.8)
ax.set_xlabel('Median Price ($)', fontsize=11, fontweight='bold')
ax.set_title('Figure 3: Top 12 Neighborhoods by Median Price', fontsize=12, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.savefig('outputs/figures/01_tour_03_top_nbhd.png', dpi=150, bbox_inches='tight')
plt.close()
figs_created += 1

# Fig 4: Proximity correlations
proximity = ['airport', 'atm', 'bank', 'bar', 'cafe', 'church', 'doctor', 'fire_station',
             'gym', 'hospital', 'library', 'park', 'parking', 'police', 'restaurant',
             'school', 'shopping_mall', 'store', 'supermarket', 'train_station']

corrs = market[proximity].corrwith(market['price']).sort_values()
fig, ax = plt.subplots(figsize=(10, 7))
colors = ['#d62728' if x < 0 else '#2ca02c' for x in corrs.values]
corrs.plot(kind='barh', ax=ax, color=colors, edgecolor='black', alpha=0.8)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel('Correlation with Sale Price', fontsize=11, fontweight='bold')
ax.set_title('Figure 4: Proximity Features — Which Drive Price UP vs DOWN?', fontsize=12, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.savefig('outputs/figures/01_tour_04_proximity_corr.png', dpi=150, bbox_inches='tight')
plt.close()
figs_created += 1

# Fig 5: CIO test (park, cafe, train)
fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))
for idx, feat in enumerate(['park', 'cafe', 'train_station']):
    with_feat = market[market[feat] > 0]['price']
    without_feat = market[market[feat] == 0]['price']

    bp = axes[idx].boxplot([without_feat, with_feat], patch_artist=True, widths=0.6)
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')

    axes[idx].set_xticklabels(['No', 'Yes'])
    axes[idx].set_ylabel('Price ($)', fontsize=10, fontweight='bold')
    axes[idx].set_title(f'{feat.replace("_", " ").title()}', fontsize=11, fontweight='bold')
    axes[idx].set_ylim(0, 850000)
    axes[idx].grid(axis='y', alpha=0.3)

    med_no = without_feat.median()
    med_yes = with_feat.median()
    pct = (med_yes - med_no) / med_no * 100
