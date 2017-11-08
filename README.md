# class_companies

## description
results for kmeans clusters on a TF-IDF matrix constructed from scraped yahoo finance, google finance, and 10-k text data from some four thousand securities.  
clusters with top-10 market-cap (mc) member names and cluster center (in the factor basis) ordered by absolute value of the projection onto that dimension are given below; 
n_clusters=11 was chosen to compare against GICS sectors

cluster 0:
centroid: [[‘services, solutions, software, data, management, company, cloud, technology, provides, security, digital, products, segment, communications, information, platform, video, enterprise, mobile']]
|                        name |           mc  |  gics_sub_industry |
| ----------------------------- | --------------- | -------------------- |
|                    APPLE INC|  794094.976211|  45202030          |          
|                 ALPHABET INC|  657848.626617|  45101010          |
|               MICROSOFT CORP|  522924.322929|  45103020          |
|                     AT&T INC|  233297.240554|  50101020          |
|                     VISA INC|  211559.697815|  45102020          |
|   VERIZON COMMUNICATIONS INC|  183734.783495|  50101020          |
|                  ORACLE CORP|  181759.542465|  45103020          |
|                   INTEL CORP|  165850.985748|  45301020          |
|            CISCO SYSTEMS INC|  157119.655798|  45201020          |
|  INTL BUSINESS MACHINES CORP|  141657.339506|  45102010          |
cluster 1:
centroid: [[‘stores, products, company, restaurants, brands, retail, accessories, apparel, food, brand, operates, segment, home, footwear, foods, states, merchandise, com, operated']]
                         |name |            mc |  gics_sub_industry
           WAL-MART STORES INC  236341.922791  30101040
                HOME DEPOT INC  187307.096329  25504030
                   PEPSICO INC  163062.898254  30201030
               MCDONALD'S CORP  119813.145523  25301040
  WALGREENS BOOTS ALLIANCE INC   88022.629905  30101010
                STARBUCKS CORP   86601.410637  25301040
                      NIKE INC   85375.360504  25203020
         COSTCO WHOLESALE CORP   74936.009681  30101040
          LOWE'S COMPANIES INC   72787.302643  25504030
    MONDELEZ INTERNATIONAL INC   68441.160278  30202030
cluster 2:
centroid: [[‘treatment, clinical, phase, company, cancer, therapeutics, development, diseases, patients, biopharmaceutical, product, pharmaceuticals, developing, stage, candidates, candidate, trial, drug, cell']]
                        |name |            mc |  gics_sub_industry
                    AMGEN INC  116274.357086  35201010
                   ABBVIE INC  104441.344030  35201010
                 CELGENE CORP   91689.401192  35201010
      BRISTOL-MYERS SQUIBB CO   88575.657990  35202010
          GILEAD SCIENCES INC   84210.010399  35201010
                   BIOGEN INC   53624.844169  35201010
    REGENERON PHARMACEUTICALS   48598.100961  35201010
   VERTEX PHARMACEUTICALS INC   29351.716469  35201010
                  INCYTE CORP   26347.805886  35201010
  ALEXION PHARMACEUTICALS INC   26134.079590  35201010

cluster 3:
centroid: [[‘investment, investments, mortgage, debt, loans, equity, securities, funds, services, capital, companies, management, invests, million, company, fund, asset, income, financial']]
                              name            mc   gics_sub_industry
1029       GOLDMAN SACHS GROUP INC  84943.354559  40203020
1060                MORGAN STANLEY  76503.752463  40203020
993                  BLACKROCK INC  62855.652022  40203010
1084  PNC FINANCIAL SVCS GROUP INC  56919.600296  40101015
1094         SCHWAB (CHARLES) CORP  51241.724034  40203020
991   BANK OF NEW YORK MELLON CORP  48042.318193  40203010
1099             STATE STREET CORP  30067.400170  40203010
990         FRANKLIN RESOURCES INC  23534.445603  40203010
1071           NORTHERN TRUST CORP  19914.289022  40203010
983     TD AMERITRADE HOLDING CORP  19298.399597  40203020

cluster 4:
centroid: [[‘estate, properties, real, trust, investment, reit, company, office, realty, ownership, invests, property, hotels, communities, shopping, self, centers, income, development']]
                           name            mc   gics_sub_industry
   SIMON PROPERTY GROUP INC  48082.260566  60101070
             PUBLIC STORAGE  37506.181407  60101080
               PROLOGIS INC  29039.766948  60101020
              WELLTOWER INC  26587.627811  60101050
  AVALONBAY COMMUNITIES INC  26435.738280  60101060
         EQUITY RESIDENTIAL  24014.481987  60101060
                 VENTAS INC  23928.412643  60101050
                    GGP INC  19761.541373  60101070
      BOSTON PROPERTIES INC  18503.446124  60101040
   DIGITAL REALTY TRUST INC  18292.843967  60101080
cluster 5:
centroid: [[‘care, products, health, medical, services, company, healthcare, surgical, diagnostic, segment, hospitals, systems, pharmaceutical, blood, therapy, patient, provides, devices, treatment']]
                          |name |            mc |  gics_sub_industry
             JOHNSON & JOHNSON  342172.590836  35202010
           PROCTER & GAMBLE CO  229101.167328  30301010
                    PFIZER INC  192283.940965  35202010
                    MERCK & CO  175086.441015  35202010
        UNITEDHEALTH GROUP INC  165449.247055  35102030
              LILLY (ELI) & CO   86254.191826  35202010
               CVS HEALTH CORP   78688.742821  30101010
           ABBOTT LABORATORIES   74581.993837  35101010
  THERMO FISHER SCIENTIFIC INC   67188.109435  35203010
          COLGATE-PALMOLIVE CO   65301.840425  30301010
cluster 6:
centroid: [[‘gas, natural, oil, energy, crude, company, exploration, basin, texas, production, gathering, properties, midstream, segment, storage, petroleum, wells, liquids, interests']]
                          |name |            mc |  gics_sub_industry
              EXXON MOBIL CORP  346374.750000  10102010
                  CHEVRON CORP  199250.531264  10102010
            NEXTERA ENERGY INC   64087.921143  55101010
              DUKE ENERGY CORP   58275.000000  55101010
                CONOCOPHILLIPS   57426.365596  10102020
  ENTERPRISE PRODS PRTNRS  -LP   56635.612403  10102040
             EOG RESOURCES INC   52928.803815  10102020
                   SOUTHERN CO   49501.192685  55101010
        DOMINION RESOURCES INC   49263.279808  55103010
     OCCIDENTAL PETROLEUM CORP   46096.632965  10102010
cluster 7:
centroid: [[‘products, systems, segment, equipment, company, industrial, power, manufactures, components, markets, solutions, materials, applications, used, services, manufacturing, technologies, control, designs']]
                         |name |            mc |  gics_sub_industry
          GENERAL ELECTRIC CO  238635.296259  20105010
             ALTRIA GROUP INC  136505.157282  30203010
                        3M CO  116605.055559  20105010
                    BOEING CO  107467.497103  20101010
  HONEYWELL INTERNATIONAL INC   99223.533015  20105010
     UNITED TECHNOLOGIES CORP   95642.526253  20101010
        TEXAS INSTRUMENTS INC   79050.149702  45301020
                  NVIDIA CORP   77845.954285  45301020
         LOCKHEED MARTIN CORP   77373.919368  20101010
                 DOW CHEMICAL   74010.755364  15101020
 
cluster 8:
centroid: [[‘insurance, life, property, casualty, products, segment, liability, company, services, reinsurance, group, commercial, health, personal, policies, coverage, financial, annuities, automobile']]
                              name            mc   gics_sub_industry
  AMERICAN INTERNATIONAL GROUP  57858.846625  40301030
                   METLIFE INC  53860.600495  40301020
                     AETNA INC  46514.289583  35102030
      PRUDENTIAL FINANCIAL INC  44410.669890  40301020
                    CIGNA CORP  41020.343264  35102030
          MARSH & MCLENNAN COS  38369.296112  40301010
             TRAVELERS COS INC  33773.871233  40301040
                 ALLSTATE CORP  30922.800446  40301040
                     AFLAC INC  29340.707926  40301020
         PROGRESSIVE CORP-OHIO  24148.012823  40301040
cluster 9:
centroid: [[‘services, company, segment, operates, water, transportation, energy, operations, provides, united, states, products, entertainment, segments, international, america, homes, management, offers']]
                         |name |            mc |  gics_sub_industry
               AMAZON.COM INC  458158.215332  25502020
                 FACEBOOK INC  427918.690613  45101010
                 COCA-COLA CO  187157.396740  30201030
                 COMCAST CORP  183410.139714  25401025
  PHILIP MORRIS INTERNATIONAL  176405.715031  30203010
             DISNEY (WALT) CO  170688.000488  25401030
             SCHLUMBERGER LTD   99216.270424  10101020
        REYNOLDS AMERICAN INC   93572.119539  30203010
    UNITED PARCEL SERVICE INC   89672.112122  20301010
          PRICELINE GROUP INC   88329.024590  25502020
cluster 10:
centroid: [[‘loans, bank, banking, services, commercial, deposit, accounts, financial, company, estate, mortgage, savings, holding, real, credit, deposits, consumer, bancorp, management']]
                        |name |            mc |  gics_sub_industry
         JPMORGAN CHASE & CO  298293.420587  40101010
            WELLS FARGO & CO  261728.984637  40101010
        BANK OF AMERICA CORP  226813.078317  40101010
               CITIGROUP INC  165415.745681  40101010
                 U S BANCORP   85840.615600  40101010
  CAPITAL ONE FINANCIAL CORP   38268.779929  40202010
                   BB&T CORP   34183.018967  40101015
          SUNTRUST BANKS INC   26262.447692  40101015
             M & T BANK CORP   24151.364442  40101015
     DISCOVER FINANCIAL SVCS   22665.826093  40202010



  *__cluster labels versus gics sector label. Columns sum to 100 and dark squares mean high overlap, e.g., gics 60 is a combination of ~80% kmeans.text cluster ‘4’ and small amplitude everywhere else.__ 
   ![alt text](https://github.com/amadeus-pinto/class_companies/blob/master/figs/heatmap.png)

