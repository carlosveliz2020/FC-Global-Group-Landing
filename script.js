/**
 * FC GLOBAL GROUP — Interactive Logic
 * Handles scroll reveals, form submissions, and nav effects.
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Scroll Reveal Animation
    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Once visible, no need to observe anymore
                observer.unobserve(entry.target);
            }
        });
    };

    const revealObserver = new IntersectionObserver(revealCallback, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // 2. Navigation Scroll Effect
    const nav = document.querySelector('.nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            nav.style.background = 'rgba(5, 5, 7, 0.95)';
            nav.style.height = '70px';
        } else {
            nav.style.background = 'rgba(5, 5, 7, 0.8)';
            nav.style.height = '80px';
        }
    });

    // 3. Smooth Scroll for Navigation Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const navHeight = 80;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 4. Form Submission Handler
    const supplierForm = document.getElementById('supplierForm');
    if (supplierForm) {
        supplierForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const submitBtn = supplierForm.querySelector('.form-submit');
            const originalText = submitBtn.textContent;
            
            // Visual feedback: Loading
            submitBtn.textContent = 'Processing...';
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.7';

            // Simulate API call
            await new Promise(resolve => setTimeout(resolve, 1500));

            // Success state
            submitBtn.textContent = '✓ Inquiry Sent Successfully';
            submitBtn.style.background = '#10B981'; // Success green
            submitBtn.style.color = '#FFFFFF';
            submitBtn.style.opacity = '1';

            // Reset form
            supplierForm.reset();

            // Revert button after delay
            setTimeout(() => {
                submitBtn.textContent = originalText;
                submitBtn.style.background = '';
                submitBtn.style.color = '';
                submitBtn.disabled = false;
            }, 4000);
        });
    }

    // 5. Parallax effect for Hero
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const heroContent = document.querySelector('.hero-content');
        if (heroContent && scrolled < 800) {
            heroContent.style.transform = `translateY(${scrolled * 0.15}px)`;
            heroContent.style.opacity = 1 - (scrolled / 800);
        }
    });

});
